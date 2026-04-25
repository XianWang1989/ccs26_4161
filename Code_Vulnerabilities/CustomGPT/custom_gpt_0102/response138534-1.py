
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Handle deletion
    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message for feedback
    flash(f"Elastic IP {ip} deleted successfully.")

    # Redirect to the page where the delete button is
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Your code to list Elastic IPs
    return render_template('elastic_ips.html', region=region)
