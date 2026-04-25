
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(
        region, 
        aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
        aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY']
    )

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    try:
        for eli in elis:
            result = eli.release()  # Assuming release() returns some status

        flash('IP address deleted successfully!', 'success')
    except Exception as e:
        flash('Error deleting IP address: {}'.format(str(e)), 'error')

    # Redirect back to the elastic IPs page
    return redirect(url_for('your_function_name', region=region))

