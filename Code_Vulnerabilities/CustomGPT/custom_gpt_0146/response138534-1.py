
from flask import redirect, request, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Process the deletion
    for eli in elis:
        r = eli.release()

    # Use flash to give feedback to the user
    flash('Elastic IP address deleted successfully!', 'success')

    # Redirect to the previous page or a specific route
    return redirect(request.referrer)  # Redirect back to the referring page
