
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        result = []
        r = eli.release()
        result.append(r)

    # Flash a message indicating that the deletion was successful
    flash(f'Elastic IP {ip} deleted successfully.')

    # Redirect back to the main page with the delete button
    return redirect(url_for('your_main_route', region=region))  # Replace 'your_main_route' with your actual route name
