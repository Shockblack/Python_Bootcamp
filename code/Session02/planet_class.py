import astropy.units as u
import astropy.constants as c
import numpy as np



class planet:

    def __init__(self, name, mass, radius, semi_major_axis, host_star, albedo=0.):
        """Class to create a planet object.

        Parameters
        ----------
        name : str
            Planet name.
        mass : float
            Planet mass in Earth masses.
        radius : float
            Planet radius in Earth radii.
        semi_major_axis : float
            Semi-major axis of the planet's orbit in AU.
        host_star : object
            Host star object.
        albedo : float, optional
            Bond albedo of the planet. Default is 0.
        """
        self.name = name

        # Check if values are in Astropy units
        self.mass = self.check_units(mass, u.M_earth)
        self.radius = self.check_units(radius, u.R_earth)
        self.semi_major_axis = self.check_units(semi_major_axis, u.au)
        
        self.host_star = host_star
        self.albedo = albedo
        

    @property
    def orbital_period(self):
        """Calculates the orbital period of a planet.

        Returns
        -------
        float
            The orbital period of the planet in days.
        """
        return np.sqrt(4*np.pi**2 * self.semi_major_axis**3 / (c.G * self.host_star.mass)).to(u.day)
    
    @property
    def surface_gravity(self):
        """Calculates the surface gravity of a planet.

        Returns
        -------
        float
            The surface gravity of the planet in m/s^2.
        """
        return (c.G * self.mass / self.radius**2).to(u.m/u.s**2)
    
    @property
    def density(self):
        """Calculates the density of a planet.

        Returns
        -------
        float
            The density of the planet in g/cm^3.
        """
        return (self.mass / (4/3 * np.pi * self.radius**3)).to(u.g/u.cm**3)
    
    @property
    def equilibrium_temperature(self):
        """Calculates the equilibrium temperature of a planet.

        Returns
        -------
        float
            The equilibrium temperature of the planet in Kelvin.
        """
        return (self.host_star.temperature * (1-self.albedo)**(1/4) * np.sqrt(self.host_star.radius / (2*self.semi_major_axis))).to(u.K)
    
    # Function to check if units are in Astropy units
    @staticmethod
    def check_units(value, unit):
        if not isinstance(value, u.Quantity):
            return value*unit
        else:
            return value
    
    
    def plot_ratio(self):
        """Plots a graphiv of the planet transiting the star."""
        import matplotlib.pyplot as plt
        from matplotlib.patches import Ellipse

        fig, ax = plt.subplots(figsize=(6,6))
        ax.set_aspect('equal')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.axis('off')

        # Plot the star
        star = plt.Circle((0, 0), 1, color='orange', alpha=0.75)
        ax.add_artist(star)
        ax.text(1/np.sqrt(2), 1/np.sqrt(2), self.host_star.name, ha='left', va='center', color='black', fontsize=12)

        # Radius ratio
        r_ratio = self.radius / self.host_star.radius
        
        # Plot the planet
        plnt = Ellipse((0, 0), r_ratio, r_ratio, color='blue')
        ax.add_artist(plnt)
        ax.text(r_ratio/np.sqrt(2), r_ratio/np.sqrt(2), self.name, ha='left', va='center', color='black', fontsize=12)

        plt.show()