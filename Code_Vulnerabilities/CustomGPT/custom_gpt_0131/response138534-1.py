
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    try:
        result = []
        for eli in elis:
            r = eli.release()
            result.append(r)
        flash('Elastic IP deleted successfully!', 'success')  # Flash a success message
    except Exception as e:
        flash(f'Error deleting Elastic IP: {str(e)}', 'danger')  # Handle any exceptions

    return redirect(url_for('your_redirect_route', region=region))  # Replace with the route you want to redirect to
