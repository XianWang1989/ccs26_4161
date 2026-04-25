
@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        eli.release()

    # Optional: Flash a success message
    flash('Elastic IP successfully deleted.')

    # Redirect back to the elastic IPs page (or any relevant page)
    return redirect(url_for('elastic_ips', region=region))
