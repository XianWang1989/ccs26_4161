
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Assuming you want to flash a message after deletion
    for eli in elis:
        r = eli.release()  # Perform the delete operation

        # Optionally flash a message to indicate success
        flash(f"Elastic IP {ip} has been deleted.", 'success')

    # Redirect back to the list of elastic IPs or the original page
    return redirect(url_for('your_list_view_function_name', region=region))
