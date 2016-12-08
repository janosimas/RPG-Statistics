# RPG Statistics

Generate some statistics about RPG tests.

## Usage

For now, just run __rpg_stats.py__, it will load the modules and show some statistics on each.

Right now it shows __numpy.stats.describe()__, not the best output...

## Contributing

### Data visualization

Include here any idea for better visualizing the data! :-D

### Creating modules

It the folder __modules__ you will find one module for each system,
they implement the methods:
- roll()
  - Return a random value of a valid roll.

These methods return a 1 or 0, for success and failure for a specialized initial character
- roll_easy()
- roll_average()
- roll_hard()

After creating a new module load it in the __rpg_stats.py__.

## Todo

- Better data visualization
- Modules initialization for user defined parameters
- More modules