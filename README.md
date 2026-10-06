# LBO-python

## Running the LBO model

'lbo.py' contains the 'easy_lbo' function, and 'run_lbo.py' is a ready-to-run example. To run it, open a terminal in the repository folder, install the dependency with 'pip install numpy', then run 'python run_lbo.py'. The script prints the entry and exit enterprise value, debt and equity, the yearly debt paydown, and the deal returns (MOIC and IRR). To test your own scenario, edit the inputs in 'run_lbo.py': entry EBITDA, entry and exit multiples, leverage, EBITDA growth, interest rate, holding period and cash sweep.

The model is intentionally simple. EBITDA grows at a constant rate, and each year the cash left after interest (EBITDA − interest) is used to repay debt according to the cash sweep percentage. At exit, equity value is the exit enterprise value minus the remaining debt. IRR is computed as MOIC^(1/years) − 1, since the only equity flows are the initial investment and the exit proceeds. Taxes, capex and working capital are not modelled, so returns are higher than in a real transaction.
