
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

    # Flash a message to indicate success
    flash(f"Elastic IP {ip} has been deleted successfully.", 'success')

    # Redirect back to the previous page (modify 'your_view' as needed)
    return redirect(url_for('your_view', region=region))

@app.route('/your_view/<region>')
def your_view(region):
    # Render your template to show the page with the delete button and list of elastic IPs
    return render_template('your_template.html', region=region)
