
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()
        flash(f'Successfully deleted Elastic IP: {ip.decode("ascii")}', 'success')  # Flash message

    return redirect(url_for('your_redirect_endpoint'))  # Redirect to the desired route

@app.route('/your_redirect_endpoint')  # Replace this with your actual endpoint
def your_redirect_endpoint():
    # Your logic to display the page with the delete button, e.g., rendering a template
    return render_template('your_template.html')  # Replace 'your_template.html' with the actual template name
