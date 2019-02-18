def ground_shipping(weight):
  if weight <= 2:
    ground_cost = weight * 1.5 + 20
    return(ground_cost)
  elif 6 >= weight > 2:
    ground_cost = weight * 3.0 + 20
    return (ground_cost)
  elif 10 >= weight > 6:
    ground_cost = weight * 4.0 + 20
    return (ground_cost)
  elif weight > 10:
    ground_cost = weight * 4.75 + 20
    return (ground_cost)

def drone_shipping(weight):
  if weight <= 2:
    drone_cost = weight * 4.5
    return(drone_cost)
  elif 6 >= weight > 2:
    drone_cost = weight * 9.0
    return (drone_cost)
  elif 10 >= weight > 6:
    drone_cost = weight * 12
    return (drone_cost)
  elif weight > 10:
    drone_cost = weight * 14.25
    return (drone_cost)

def shipping(weight):
    ground_cost = ground_shipping(weight)
    drone_cost = drone_shipping(weight)
    premium_shipping = 125
    if ground_cost > drone_cost and drone_cost < premium_shipping:
        print("The best way is shipping by drone! Cost:", drone_cost)
    elif drone_cost > ground_cost and ground_cost < premium_shipping:
        print("The best way is ground shipping! Cost:", ground_cost)
    else:
        print("The best option is premium shipping. Cost:", premium_shipping)

print("This program will choose the best shipping option for you!")
weight=input("What is weight of the package?")
shipping(float(weight))