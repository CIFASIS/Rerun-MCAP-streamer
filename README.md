# Rerun MCAP streamer

This script makes it possible to work with MCAP files 'Bigger than RAM' in Rerun by reading them sequentially and 
logging the data as it comes.

It was made to be used with the Rosario Dataset V2, but we're working on making it useful for any recording.

## Usage

Before using the script, ensure that all dependencies are installed by running `pip install -r requirements.txt` 
(preferably inside a virtual environment). For example

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Then use the script by running

```bash
python3 rerun_batch.py [-h] -b BAG_PATH [-m MEMORY_LIMIT] [--header_timestamp]
                                        [--urdf URDF] [--blueprints BLUEPRINTS]
```

Once it starts it displays the controls, which allow to quit, pause, and change the current blueprint.

## Blueprints

Rerun has a filetype to save how the viewer is currently setup, which they call a 'Blueprint'.
These blueprints allow to see the information in different ways, depending which container type is used.

We can quickly change between blueprints by logging the files saved in the './blueprints' directory (or the one set in the --blueprints option).

