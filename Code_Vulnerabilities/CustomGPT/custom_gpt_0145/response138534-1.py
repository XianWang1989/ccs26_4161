
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Optionally, you can set a flash message to inform the user about the deletion
    flash(f'Elastic IP {ip} deleted successfully.')

    # Redirecting back to the main page or the page from which the delete was called
    return redirect(url_for('your_route_name', region=region))  # Replace 'your_route_name' with your actual route name

# Remember to define the 'your_route_name' route for the redirect to work
@app.route('/elastic_ips/<region>')
def your_route_name(region):
    # Logic for rendering the page where the delete button is located
    pass
