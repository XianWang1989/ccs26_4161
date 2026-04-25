
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

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

    flash("IP address deleted successfully.")  # Show a success message
    return redirect(url_for('your_redirect_route', region=region))  # Replace with your actual route

@app.route('/elastic_ips/<region>')
def your_redirect_route(region):
    # Your logic to render the relevant page
    return render_template('your_template.html', region=region)
