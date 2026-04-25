
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()  # Assuming this returns some confirmation
        flash(f'Successfully deleted IP: {ip}')  # Show a message on redirect

    # Redirect to the main page (or any other route)
    return redirect(url_for('your_target_view', region=region))

@app.route('/elastic_ips/<region>')
def your_target_view(region):
    # Your code to display the list of elastic IPs for the region
    return render_template('your_template.html', region=region)
