
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

    # Flash a message to indicate success or failure
    flash("Deleted Elastic IP: {}".format(ip.decode('ascii')), "success")

    # Redirect back to the page with the delete button (you can adjust the view as needed)
    return redirect(url_for('your_view_function_name', region=region))

@app.route('/elastic_ips/<region>')
def your_view_function_name(region):
    # Your logic to display Elastic IPs
    return render_template('your_template.html', region=region)
