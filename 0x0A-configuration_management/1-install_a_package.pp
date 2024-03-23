# Install an especific version of flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/local/bin', '/usr/bin'],
  environment => ['PIP_DISABLE_PIP_VERSION_CHECK=1'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require     => Package['python3-pip'],
}
