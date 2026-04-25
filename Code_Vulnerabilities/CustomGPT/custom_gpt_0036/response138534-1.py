
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
        r = eli.release()  # Release the elastic IP

    # Flashing a success message
    flash(f'Successfully deleted the Elastic IP: {ip.decode("ascii")}', 'success')

    # Redirect to the page that shows the list of IPs or a relevant page
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to display the list of Elastic IPs
    return render_template('elastic_ips_list.html', region=region)
