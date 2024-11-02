## Repository Structure
```
├── data/                     # Directory for storing raw data files
│   ├── raw/                  # Raw data files from APIs (optional)
│   └── processed/            # Processed data files (optional)
│
├── docs/                     # Documentation files
│   ├── README.md             # Project overview and instructions
│   └── API_Usage.md          # Detailed information about the APIs used
│
├── scripts/                  # Main source code for the project
│   ├── main.py               # Entry point of the application
│   ├── api_fetcher.py        ✅ # Module to handle API calls
│   ├── data_fetcher.py       ✅ # Module to fetch data from the API
│   ├── data_processor.py     # Module for data processing and cleaning
│   └── visualizer.py         # Module for generating visualizations
│
├── tests/                    # Tests for the code
│   ├── test_api_fetcher.py   # Tests for the API fetching module
│   ├── test_data_processor.py # Tests for the data processing module
│   └── test_visualizer.py     # Tests for the visualizer module
│
├── requirements.txt          # List of dependencies (libraries)
│
├── .gitignore                # Ignore files for Git
├── .env                      # Confidential funnies: Contains ALPHA_VANTAGE_API_KEY
│
└── README.md                 # Project overview and instructions