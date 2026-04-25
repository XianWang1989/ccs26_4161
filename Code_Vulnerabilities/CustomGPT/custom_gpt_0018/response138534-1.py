
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optional: Flash a message to inform the user
    flash('Elastic IP deleted successfully!')

    # Redirect back to the page where the delete button was
    return redirect(url_for('your_view_function_name', region=region))  # replace 'your_view_function_name' with your actual route function name
