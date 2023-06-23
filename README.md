# MP3Player

## Requirements

Install the following python packages:

- beets
- tk
- pygame

## Beets Setup

You’ll want to set a few basic options before you start using beets. The configuration is stored in a text file. You can show its location by running `beet config -p`, though it may not exist yet. Run `beet config -e` to edit the configuration in your text editor. The file will start out empty, but here’s good place to start:

```yaml
directory: ~/music
library: ~/data/musiclibrary.db
```

Change that first path to a directory where you’d like to keep your music. Then, for library, choose a good place to keep a database file that keeps an index of your music. (The config’s format is YAML. You’ll want to configure your text editor to use spaces, not real tabs, for indentation. Also, ~ means your home directory in these paths, even on Windows.)
