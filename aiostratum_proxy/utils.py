from datetime import datetime, timezone
from importlib import import_module

from . import app_version


def import_from_module(s):
    p, m = s.rsplit('.', 1)
    mod = import_module(p)
    return getattr(mod, m)


default_config = """# This file was generated by {app_version} on {generated_datetime}

proxies:
- ## Optional name to give your log output some flair and order

  #name: ''

  ## max_workers allows the proxy to ensure each worker up to this limit
  ## has a unique nonce-space in which to generate solutions, avoiding
  ## duplicate shares from multiple rigs.
  ## Options are 1 (solo mode), 256 (the default), or 65536

  #max_workers: 256

  ## Some pools for some algorithms support sending out a new extra_nonce1
  ## value to connected workers; some pools do not support this, and will
  ## disconnect immediately if this is set to true

  #extranonce_subscribe: false

  ## These two lines define the aiostratum_proxy Python classes you
  ## want to use to handle this proxy's workers and pool connections

  worker_class: aiostratum_proxy.protocols.equihash.EquihashWorkerProtocol
  pool_class: aiostratum_proxy.protocols.equihash.EquihashPoolProtocol

  ## This is a list of host/port pairs to which your workers can connect
  ## to this proxy; blank `host` (the default) means listen on all available
  ## interfaces (all private/public IPs; both IPv4/6)

  listen:
  - host: ''
    port: 10666
  # - host: ''
  #   port: 10667
  #   ## TLS/SSL supported; add another port listening for TLS/SSL connections
  #   ssl: true
  #   ssl_cert_file: '<path to your ssl cert file>'
  #   ssl_cert_key_file: '<path to your ssl cert key file>'

  ## This is the list of pools (at least 1 required, obviously) to have the
  ## proxy connect to

  pools:
  - name: Example primary pool
    host: btcp.pooldomain.io
    port: 9000
    account_name: poolaccountnameoraddress1.rig1
    account_password: poolaccountpassword
  # - name: Example fallback pool #1
  #   host: btcp.anotherpooldomain.io
  #   port: 9001
  #   ## Miner login credentials for pool
  #   account_name: poolaccountnameoraddress2.rig1
  #   account_password: poolaccountpassword
  #   ## TLS/SSL pool connection? (check with your pool operator if supported),
  #   ## and should the SSL connection verify the server's certificate?
  #   ssl: true
  #   ssl_verify: false
""".format(
    app_version=app_version,
    generated_datetime=datetime.now(timezone.utc).astimezone().isoformat()
)


def output_config():
    print(default_config)
