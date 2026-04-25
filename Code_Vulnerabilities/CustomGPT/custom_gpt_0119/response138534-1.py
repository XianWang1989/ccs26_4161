
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()
        # You could flash a success message here if you want
        flash(f'Successfully deleted IP: {ip}')

    # Redirect back to the list of Elastic IPs after deletion
    return redirect(url_for('your_list_route', region=region))  # replace 'your_list_route' with the actual route name
