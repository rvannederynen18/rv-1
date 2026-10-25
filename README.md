# RV-1

Ryan's home station: a control-panel style dashboard for the day. Schedule, weather, tides, sports, market check, local events, rocket launches, news, garage, tools and favorite links, with voice commands and a spoken briefing.

**Open it here:** https://rvannederynen18.github.io/rv-1/

- `index.html` is the whole app, built from `src/` by `build.py`. Don't edit `index.html` by hand: change `src/rv1.html`, then run `python3 build.py`.
- `data.json` is refreshed each morning with public data (market, local events, extra team scores). `version.json` tells the downloaded `rv-1.html` when an update is ready.
- Nothing personal is in the code. Name, address, calendar email and other settings are entered under **Life → Settings** and saved only in the browser on each device.
- To move your setup to another device: **Life → Save backup file**, then **Life → Restore from file** on the new device. Keep backup files out of this repo, since it's public.
- Phone: open the link in Safari, tap **Share → Add to Home Screen**. The **Phone view / Full view** button in the top bar switches layouts.
- For a big screen: open the link on the PC and press **Full screen** in the top bar. Esc returns to normal view.
- Uses free live data (NOAA, National Weather Service, Open-Meteo, ESPN, The Space Devs, Queue-Times), so it needs internet.

To update the downloaded `rv-1.html`: when the **Update** banner appears, tap **Download it** and replace the old file with the new one, same name and folder.

Settings, data status and backup are under **Life → Settings, status & backup**.
