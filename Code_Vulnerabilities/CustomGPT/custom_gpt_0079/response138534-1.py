
from flask import Flask, redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()
        # Optionally, you can flash a message to be shown after redirect
        flash(f'Elastic IP {ip} deleted successfully!')

    # Redirect back to the list of Elastic IPs
    return redirect(url_for('elastic_ips_view', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips_view(region):
    # Your logic to display elastic IPs
    return render_template('elastic_ips.html', region=region)
