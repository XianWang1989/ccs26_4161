
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

@app.route('/elastic_ips/<region>/delete/<ip>', methods=['POST'])
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

    flash('Elastic IP deleted successfully!', 'success')  # Show a success message
    return redirect(url_for('your_desired_route', region=region))  # Redirect back to the desired page

@app.route('/elastic_ips/<region>')
def your_desired_route(region):
    # Render the page showing your elastic IPs or whatever logic you have
    return render_template('your_template.html', region=region)

# Add this route for your delete link to work properly
@app.route('/some_page/<region>')
def some_page(region):
    # Logic for this page
    return "Some content here"
