### Tasks

1. **Identify top math-performing schools**

   * Select schools where the average math score is **at least 80% of the maximum possible (≥ 640 out of 800)**.
   * Save results in a DataFrame named `best_math_schools` with the following columns:

     * `school_name`
     * `average_math`
   * Sort the results by `average_math` in **descending order**.

2. **Find the top 10 schools by combined SAT scores**

   * Create a new column `total_SAT` as the sum of math, reading, and writing scores.
   * Save results in a DataFrame named `top_10_schools` with the following columns:

     * `school_name`
     * `total_SAT`
   * Order results by `total_SAT` in **descending order** and select the top 10 schools.

3. **Determine borough with largest score variability**

   * Group schools by borough and compute statistics on `total_SAT`.
   * Save results in a DataFrame named `largest_std_dev` containing **only one row** with:

     * `borough` – the name of the borough with the **largest standard deviation** in `total_SAT`.
     * `num_schools` – number of schools in that borough.
     * `average_SAT` – mean of `total_SAT`.
     * `std_SAT` – standard deviation of `total_SAT`.
   * Round all numeric values to **two decimal places**.
