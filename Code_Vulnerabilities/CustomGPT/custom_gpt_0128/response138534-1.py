
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()  # Perform the delete operation

    flash('Elastic IP deleted successfully!', 'success')  # Optional: add a flash message
    return redirect(url_for('your_desired_route', region=region))  # Redirect to the desired route

@app.route('/elastic_ips/<region>')
def your_desired_route(region):
    # Your code to display the list of elastic IPs or any relevant information
    return render_template('your_template.html', region=region)
