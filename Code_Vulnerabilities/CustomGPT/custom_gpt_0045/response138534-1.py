
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Assume we use a variable to keep track of deletion status
    deletion_success = True
    for eli in elis:
        r = eli.release()
        if r:  # Check if the deletion was successful
            continue
        else:
            deletion_success = False  # Mark as failure if any deletion fails

    # Flash a message based on the operation success
    if deletion_success:
        flash('Elastic IP deleted successfully!', 'success')
    else:
        flash('Failed to delete Elastic IP.', 'error')

    # Redirect back to the page where the delete button is located
    return redirect(url_for('your_page_name', region=region))  # replace 'your_page_name' with the actual function name of the page
