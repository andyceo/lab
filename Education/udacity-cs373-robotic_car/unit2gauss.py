def gauss(x, mu, sigma_square):
  x, mu, sigma_square = float(x), float(mu), float(sigma_square)
  pi = 3.14159
  e = 2.718281828
  k = 1.0 / (2*pi*sigma_square) ** (1.0/2.0)
  power = -((x - mu) ** 2) / (2*sigma_square)
  return k * e ** power

print(gauss(8, 10, 4))


def get_sigma2(sigma2, sigma2Measurement):
  return 1.0 / (1.0 / sigma2 + 1.0 / sigma2Measurement)

def get_mu(mu, sigma2, muMeasurement, sigma2Measurement):
  return (1.0 / (sigma2 + sigma2Measurement)) * (sigma2Measurement*mu + sigma2*muMeasurement)

print(get_mu(10., 4., 12., 4.))
print(get_sigma2(4., 4.))

print(get_mu(10., 8., 13., 2.))
print(get_sigma2(8., 2.))

print(get_mu(10., 4., 10., 4.))
print(get_sigma2(4., 4.))
