# Hong Kong Translation Evaluation

This repo contains a set of text mostly related to political events from Hong Kong for testing the performance of machine translation apis. The text are written with Traditional Chinese, and could be in Hong Kongese or Standard Chinese. Sources include personal accounts, public statements, forum posts and news articles.

## Directories

* aws       - translated by aws.
* azure     - translated by azure.
* google    - translated by google.
* original  - original text that needs to be translated.
* reference - human translated version.

## Results

### 兄弟爬山，各自努力。

* aws    - Brothers climbing mountains, each working hard.
* azure  - Brothers climb mountains, each effort.
* google - Brothers climb the mountain and work hard.

### BLEU scores

* aws    - 0.12242330341350044
* azure  - 0.11080583668555727
* google - 0.10324928524127852

### NIST scores

* aws    - 4.914027424232511
* azure  - 4.787966671498649
* google - 4.48820715693543
