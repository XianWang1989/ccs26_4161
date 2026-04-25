
from flask import Flask, redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    success = False
    for eli in elis:
        r = eli.release()
        if r:  # Assuming r indicates success
            success = True

    # Optionally add a flash message
    if success:
        flash('Elastic IP deleted successfully.', 'success')
    else:
        flash('Failed to delete Elastic IP.', 'error')

    # Redirect back to the relevant page
    return redirect(url_for('your_view_function', region=region))

# Note: Replace 'your_view_function' with the actual function name that renders your page.
