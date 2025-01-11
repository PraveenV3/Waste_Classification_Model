import os
import splitfolders

# Define paths
input_dir = "data"  # Folder containing 6 waste categories
output_dir = "processed_data"  # Folder to save split datasets

# Split the dataset into train, test, and validation sets
splitfolders.ratio(
    input_dir,
    output=output_dir,
    seed=42,  # Random seed for reproducibility
    ratio=(0.7, 0.2, 0.1),  # Train 70%, Test 20%, Validation 10%
    group_prefix=None,  # Don't group files by prefix
    move=False,  # Copy files instead of moving them
)

print("Dataset split completed!")