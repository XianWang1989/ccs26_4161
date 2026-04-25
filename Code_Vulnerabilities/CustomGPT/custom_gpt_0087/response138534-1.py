
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(
        region, 
        aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
        aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY']
    )
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optionally flash a success message
    flash('Elastic IP deleted successfully!')

    # Redirect back to the relevant page
    return redirect(url_for('your_route_name', region=region))  # Replace 'your_route_name' with the actual route name

@app.route('/elastic_ips/<region>')
def your_route_name(region):
    # Your code to render the page that lists the Elastic IPs
    return render_template('your_template.html', region=region)
