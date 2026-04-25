
from flask import Flask, redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        try:
            r = eli.release()
            flash('Elastic IP deleted successfully.', 'success')
        except Exception as e:
            flash(f'Failed to delete Elastic IP: {str(e)}', 'error')

    # Redirect back to the main elastic IPs page or a specified route
    return redirect(url_for('your_desired_route', region=region))  # Replace 'your_desired_route' with the actual route name
