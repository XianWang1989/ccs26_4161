
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

    # Flash a message to indicate success or failure
    flash('Elastic IP deleted successfully.', 'success')

    # Redirect back to the region's elastic IPs page
    return redirect(url_for('view_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def view_elastic_ips(region):
    # Your logic to display elastic IPs for the region
    # Render a template or return a response here
