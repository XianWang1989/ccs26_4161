
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
        r = eli.release()  # Perform the deletion
        result.append(r)

    # Optionally, you can use flash to send a message if you have message handling set up
    flash(f'Elastic IP {ip} deleted successfully.', 'success') 

    # Redirect to the appropriate route (e.g., back to a list of Elastic IPs)
    return redirect(url_for('view_elastic_ips', region=region))
