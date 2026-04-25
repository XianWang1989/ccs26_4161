
from flask import Flask, redirect, url_for, request, flash

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()
        # You could also flash a message to the user
        flash(f'Successfully deleted IP: {ip.decode("ascii")}')

    # Redirecting to the main page or the same page after deletion
    return redirect(url_for('show_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def show_elastic_ips(region):
    # This is where you would render the list of elastic IPs
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
