
from flask import Flask, redirect, url_for, flash
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

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

    # Flash a message to inform the user about the result
    flash(f"Successfully deleted IP: {ip.decode('ascii')}" if result else "No IP found to delete.")

    # Redirect back to the page where the delete button was
    return redirect(url_for('your_target_route', region=region))

@app.route('/your_target_route/<region>')
def your_target_route(region):
    # This would be the page with your delete button and other UI elements
    return render_template('your_template.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
