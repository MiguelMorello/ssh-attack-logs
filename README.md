# SSH Log Analysis

This project analyzes SSH log data to identify potential malicious activities, such as brute force attacks, invalid login attempts, and other suspicious behavior. The data is extracted from log files and then processed using Python for exploratory data analysis (EDA), visualization, and correlation analysis.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Code Analysis](#code-analysis)
- [Results](#results)
- [Discussion](#discussion)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)
- [Contributing](#contributing)
- [License](#license)

## Introduction

SSH (Secure Shell) is a widely-used protocol for remote login. It is essential to monitor SSH logs to detect potential security threats, including brute force attacks, unauthorized access attempts, and compromised servers. This project aims to analyze a dataset of SSH logs, identify trends, and provide insights into the nature of SSH-based attacks.

## Dataset

The dataset used in this project is derived from log files of SSH connections. These logs record various details, such as IP addresses, timestamps, success or failure of connections, and additional flags indicating suspicious behavior. The dataset includes the following features:
- `is_private`: Whether the IP is private or not.
- `is_failure`: Indicates if the login attempt was a failure.
- `is_root`: Whether the login attempt was attempting to access the root user.
- `is_valid`: Whether the login attempt was valid.
- `class`: The class of the attack (malicious or non-malicious).
- `timestamp (ts)`: The timestamp of the login attempt.

## Methodology

The methodology includes:
1. **Data Loading**: Loading the dataset from a CSV file using `pandas`.
2. **Exploratory Data Analysis (EDA)**: Analyzing the distribution of variables and identifying missing values.
3. **Visualization**: Using `matplotlib` and `seaborn` to create visualizations such as:
   - Count plots for binary variables.
   - Correlation heatmaps for numeric variables.
   - Time series plots for trend analysis.
4. **Feature Extraction**: Parsing the SSH log files to extract relevant features.

## Code Analysis

The Python code leverages the following libraries:
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization, including heatmaps and line plots.
- **Numpy**: For numerical operations.
  
The code performs the following steps:
1. Loads the dataset using `pandas.read_csv()`.
2. Conducts exploratory data analysis (EDA) to inspect the dataset, handle missing values, and analyze feature distributions.
3. Creates various visualizations, such as:
   - Distribution of binary variables (`is_private`, `is_failure`, `is_root`, `is_valid`, `class`).
   - Correlation matrix of numeric features.
   - Temporal trends of failures and successful logins.
4. Provides a detailed view of the dataset to help identify patterns in SSH logins.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('path_to_your_data/SSH.csv')

# Analysis function
def analyze_ssh_data(data):
    # EDA
    print(data.info())
    print(data.head())
    # Visualizations
    # ... (remaining code here)

analyze_ssh_data(data)
```

## Results

Key findings include:
- **Failed Attempts**: A significant number of login attempts were unsuccessful, suggesting possible brute-force attacks.
- **Root Access**: Some login attempts were made with the `root` user, which is a critical concern for system security.
- **Valid Access**: Over time, more valid login attempts were observed, indicating that security measures may have been applied.
- **Correlations**: Several correlations between variables such as `is_failure`, `is_valid`, and `class` were observed. Notably, there was a strong positive correlation between `ip_failure` and `class` (malicious activity).

## Discussion

The analysis revealed important trends in SSH log behavior:
- **Malicious Activities**: A high number of failed login attempts and activities related to root access suggest potential brute-force attacks.
- **Security Measures**: Over time, the number of successful logins increased, possibly due to the application of better security protocols, such as firewall rules or IP blocking.
- **Feature Correlation**: A high correlation between features like `ip_failure`, `not_valid_count`, and `class` indicates that repeated failed attempts may be a strong indicator of malicious activity.

## Conclusion

The dataset reveals that SSH servers are frequently targeted by brute-force attacks and other unauthorized attempts. The findings highlight the importance of continuous monitoring and the implementation of security measures like IP blocking, strong authentication mechanisms, and proactive alerting systems.

## How to Run

To run the analysis, you need to have Python and the necessary dependencies installed. Follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ssh-log-analysis.git
   cd ssh-log-analysis
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis:
   ```bash
   python analysis.py
   ```

Make sure to replace `'path_to_your_data/SSH.csv'` with the actual path to your dataset.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to fix bugs, please follow the steps below:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to update placeholders (such as file paths and GitHub links) accordingly!
