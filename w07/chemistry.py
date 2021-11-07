def make_periodic_table():
    return [
        # [symbol, name, atomic_mass]
        ['Ac', 'Actinium', 227],
        ['Al', 'Aluminum', 26.9815386],
        ['Am', 'Americium', 243],
        ['Sb', 'Antimony', 121.76],
        ['Ar', 'Argon', 39.948],
        ['As', 'Arsenic', 74.9216],
        ['At', 'Astatine', 210],
        ['Ba', 'Barium', 137.327],
        ['Bk', 'Berkelium', 247],
        ['Be', 'Beryllium', 9.012182],
        ['Bi', 'Bismuth', 208.9804],
        ['Bh', 'Bohrium', 272],
        ['B', 'Boron', 10.811],
        ['Br', 'Bromine', 79.904],
        ['Cd', 'Cadmium', 112.411],
        ['Ca', 'Calcium', 40.078],
        ['Cf', 'Californium', 251],
        ['C', 'Carbon', 12.0107],
        ['Ce', 'Cerium', 140.116],
        ['Cs', 'Cesium', 132.9054519],
        ['Cl', 'Chlorine', 35.453],
        ['Cr', 'Chromium', 51.9961],
        ['Co', 'Cobalt', 58.933195],
        ['Cn', 'Copernicium', 285],
        ['Cu', 'Copper', 63.546],
        ['Cm', 'Curium', 247],
        ['Ds', 'Darmstadtium', 281],
        ['Db', 'Dubnium', 268],
        ['Dy', 'Dysprosium', 162.5],
        ['Es', 'Einsteinium', 252],
        ['Er', 'Erbium', 167.259],
        ['Eu', 'Europium', 151.964],
        ['Fm', 'Fermium', 257],
        ['Fl', 'Flerovium', 289],
        ['F', 'Fluorine', 18.9984032],
        ['Fr', 'Francium', 223],
        ['Gd', 'Gadolinium', 157.25],
        ['Ga', 'Gallium', 69.723],
        ['Ge', 'Germanium', 72.64],
        ['Au', 'Gold', 196.966569],
        ['Hf', 'Hafnium', 178.49],
        ['Hs', 'Hassium', 270],
        ['He', 'Helium', 4.002602],
        ['Ho', 'Holmium', 164.93032],
        ['H', 'Hydrogen', 1.00794],
        ['In', 'Indium', 114.818],
        ['I', 'Iodine', 126.90447],
        ['Ir', 'Iridium', 192.217],
        ['Fe', 'Iron', 55.845],
        ['Kr', 'Krypton', 83.798],
        ['La', 'Lanthanum', 138.90547],
        ['Lr', 'Lawrencium', 262],
        ['Pb', 'Lead', 207.2],
        ['Li', 'Lithium', 6.941],
        ['Lv', 'Livermorium', 293],
        ['Lu', 'Lutetium', 174.9668],
        ['Mg', 'Magnesium', 24.305],
        ['Mn', 'Manganese', 54.938045],
        ['Mt', 'Meitnerium', 276],
        ['Md', 'Mendelevium', 258],
        ['Hg', 'Mercury', 200.59],
        ['Mo', 'Molybdenum', 95.96],
        ['Mc', 'Moscovium', 288],
        ['Nd', 'Neodymium', 144.242],
        ['Ne', 'Neon', 20.1797],
        ['Np', 'Neptunium', 237],
        ['Ni', 'Nickel', 58.6934],
        ['Nh', 'Nihonium', 284],
        ['Nb', 'Niobium', 92.90638],
        ['N', 'Nitrogen', 14.0067],
        ['No', 'Nobelium', 259],
        ['Og', 'Oganesson', 294],
        ['Os', 'Osmium', 190.23],
        ['O', 'Oxygen', 15.9994],
        ['Pd', 'Palladium', 106.42],
        ['P', 'Phosphorus', 30.973762],
        ['Pt', 'Platinum', 195.084],
        ['Pu', 'Plutonium', 244],
        ['Po', 'Polonium', 209],
        ['K', 'Potassium', 39.0983],
        ['Pr', 'Praseodymium', 140.90765],
        ['Pm', 'Promethium', 145],
        ['Pa', 'Protactinium', 231.03588],
        ['Ra', 'Radium', 226],
        ['Rn', 'Radon', 222],
        ['Re', 'Rhenium', 186.207],
        ['Rh', 'Rhodium', 102.9055],
        ['Rg', 'Roentgenium', 280],
        ['Rb', 'Rubidium', 85.4678],
        ['Ru', 'Ruthenium', 101.07],
        ['Rf', 'Rutherfordium', 267],
        ['Sm', 'Samarium', 150.36],
        ['Sc', 'Scandium', 44.955912],
        ['Sg', 'Seaborgium', 271],
        ['Se', 'Selenium', 78.96],
        ['Si', 'Silicon', 28.0855],
        ['Ag', 'Silver', 107.8682],
        ['Na', 'Sodium', 22.98976928],
        ['Sr', 'Strontium', 87.62],
        ['S', 'Sulfur', 32.065],
        ['Ta', 'Tantalum', 180.94788],
        ['Tc', 'Technetium', 98],
        ['Te', 'Tellurium', 127.6],
        ['Ts', 'Tennessine', 294],
        ['Tb', 'Terbium', 158.92535],
        ['Tl', 'Thallium', 204.3833],
        ['Th', 'Thorium', 232.03806],
        ['Tm', 'Thulium', 168.93421],
        ['Sn', 'Tin', 118.71],
        ['Ti', 'Titanium', 47.867],
        ['W', 'Tungsten', 183.84],
        ['U', 'Uranium', 238.02891],
        ['V', 'Vanadium', 50.9415],
        ['Xe', 'Xenon', 131.293],
        ['Yb', 'Ytterbium', 173.054],
        ['Y', 'Yttrium', 88.90585],
        ['Zn', 'Zinc', 65.38],
        ['Zr', 'Zirconium', 91.224],
    ]


def main():
    print(make_periodic_table())


if __name__ == "__main__":
    main()
