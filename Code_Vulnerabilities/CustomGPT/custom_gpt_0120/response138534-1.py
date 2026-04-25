
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

    # Optionally, you can flash a message to inform the user
    flash('Elastic IP deleted successfully!', 'success')

    # Redirect to the elastic IPs page or another relevant route
    return redirect(url_for('elastic_ips_page', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips_page(region):
    # Logic to display the elastic IPs for the given region
    return render_template('elastic_ips.html', region=region)
