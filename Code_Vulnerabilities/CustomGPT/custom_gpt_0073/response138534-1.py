
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    try:
        for eli in elis:
            eli.release()  # Release the Elastic IP

        flash('Elastic IP deleted successfully!', 'success')  # Flash message for user feedback
    except Exception as e:
        flash(f'Error deleting Elastic IP: {str(e)}', 'error')  # Handle errors

    return redirect(url_for('your_view_function_name', region=region))  # Redirect back to the relevant view
