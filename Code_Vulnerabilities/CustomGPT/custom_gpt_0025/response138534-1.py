
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Redirecting back to the main page (or wherever appropriate)
    return redirect(url_for('your_target_route', region=region))

@app.route('/your_target_route/<region>')
def your_target_route(region):
    # Render your main page with the delete button here
    return render_template('your_template.html', region=region)
