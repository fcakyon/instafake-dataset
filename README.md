# InstaFake Dataset
Dataset of the [Intagram Fake and Automated Account Detection](https://arxiv.org/pdf/1910.03090.pdf) paper

### Installation

##### Install miniconda
https://conda.io/en/latest/miniconda.html

##### Setup a CONDA environment
We create a new vitrual environment named `instafake`.
```
conda create --name instafake python=3.6
```

##### Activating the virtual environment
If you are inside the virtual environment, your shell prompt should look like: `(instafake) user@computer:~$`
If that is not the case, you can enable the virtual environment using:
```
conda activate instafake 
```
To deactivate the virtual environment, use:
```
conda deactivate
```

##### Install required packages

To install the required packages, run the following command in your `instafake` virtual environment:
```
pip install -r requirements.txt
```

### Import Datasets as Dataframes
To import the fake and automated datasets as pandas dataframes, simply define the dataset folder path `data`, and dataset version  `dataset_version` and call `import_data` from `utils`:

~~~py
from utils import import_data

dataset_path = "data"
dataset_version = "fake-v1.0"

fake_dataset = import_data(dataset_path, dataset_version)

dataset_path = "data"
dataset_version = "automated-v1.0"

automated_dataset = import_data(dataset_path, dataset_version)
~~~

### Dataset Structures

The dataset contains of 2 set of json files with given features:

##### Fake Account Detection
1. `user_media_count` - Total number of posts, an account has.
2. `user_follower_count` - Total number of followers, an account has.
3. `user_following_count` - Total number of followings, an account has.
4. `user_has_profil_pic` - Whether an account has a profil picture, or not.
5. `user_is_private` - Whether an account is a private profile, or not.
6. `user_biography_length` - Number of characters present in account biography.
7. `username_length` - Number of characters present in account username.
8. `username_digit_count` - Number of digits present in account username.
9. `is_fake` - True, if account is a spam/fake account, False otherwise

##### Automated Account Detection
1. `user_media_count` - Total number of posts, an account has.
2. `user_follower_count` - Total number of followers, an account has.
3. `user_following_count` - Total number of followings, an account has.
4. `user_has_highlight_reels` - Whether an account has at least one highlight reel present, or not.
5. `user_has_url` - Whether an account has an url present in biography, or not.
6. `user_biography_length` - Number of characters present in account biography.
7. `username_length` - Number of characters present in account username.
8. `username_digit_count` - Number of digits present in account username.
9. `media_comment_numbers` - Total number of comments for a given media.
10. `media_comments_are_disabled` - Whether given media is closed for comments, or not.
11. `media_has_location_info` - Whether given media includes location, or not.
12. `media_hashtag_numbers` - Total number of hashtags, given media has.
13. `media_upload_times` - Media upload timastamps.
14. `automated_behaviour` - True, if account is an automated account, False otherwise

### Dataset Metadata
The following table is necessary for this dataset to be indexed by search
engines such as <a href="https://g.co/datasetsearch">Google Dataset Search</a>.
<div itemscope itemtype="http://schema.org/Dataset">
<table>
  <tr>
    <th>property</th>
    <th>value</th>
  </tr>
  <tr>
    <td>name</td>
    <td><code itemprop="name">InstaFake Dataset: An Instagram fake and automated account detection dataset</code></td>
  </tr>
  <tr>
    <td>alternateName</td>
    <td><code itemprop="alternateName">InstaFake Dataset</code></td>
  </tr>
  <tr>
    <td>url</td>
    <td><code itemprop="url">https://github.com/fcakyon/instafake-dataset</code></td>
  </tr>
  <tr>
    <td>sameAs</td>
    <td><code itemprop="sameAs">https://github.com/fcakyon/instafake-dataset</code></td>
  </tr>
    <tr>
    <td>sameAs</td>
    <td><code itemprop="sameAs">https://github.com/fcakyon/instafake-dataset</code></td>
  </tr>
  <tr>
    <td>description</td>
    <td><code itemprop="description">The InstaFake Dataset is comprised of anonymized Instagram user data collected by Fatih Cagatay Akyon and Esat Kalfaoglu over the second half of 2018. We’re releasing this dataset publicly to aid the research community in making advancements in machine learning based social media analysis.</code></td>
  </tr>
  <tr>
    <td>provider</td>
    <td>
      <div itemscope itemtype="http://schema.org/Organization" itemprop="provider">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">Fatih C. Akyon and Esat Kalfaoglu</code></td>
          </tr>
          <tr>
            <td>sameAs</td>
            <td><code itemprop="sameAs">https://scholar.google.com.tr/citations?user=RHGyDE0AAAAJ&hl=en</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
  <tr>
    <td>license</td>
    <td>
      <div itemscope itemtype="http://schema.org/CreativeWork" itemprop="license">
        <table>
          <tr>
            <th>property</th>
            <th>value</th>
          </tr>
          <tr>
            <td>name</td>
            <td><code itemprop="name">Attribution-NonCommercial</code></td>
          </tr>
          <tr>
            <td>url</td>
            <td><code itemprop="url">https://creativecommons.org/licenses/by-nc/4.0//</code></td>
          </tr>
        </table>
      </div>
    </td>
  </tr>
</table>
</div>
