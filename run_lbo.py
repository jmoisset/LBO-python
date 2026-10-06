from lbo import easy_lbo

r = easy_lbo(
    entry_ebitda=10,        # EBITDA d'entrée (M€)
    entry_multiple=8,       # VE = 8x EBITDA
    leverage_multiple=5,    # dette = 5x EBITDA
    ebitda_growth=0.05,     # +5 %/an
    years=5,                # durée de détention
    interest_rate=0.07,     # 7 % de taux
    exit_multiple=8,        # sortie à 8x
    cash_sweep=1.0,         # 100 % du cash rembourse la dette
)

print(f"VE entrée : {r['ev_entry']:.1f} | Dette : {r['debt_entry']:.1f} | Equity : {r['equity_entry']:.1f}")
print(f"VE sortie : {r['ev_exit']:.1f} | Dette restante : {r['final_debt']:.1f} | Equity : {r['equity_exit']:.1f}")
print(f"MOIC : {r['moic']:.2f}x | TRI : {r['irr']:.1%}")
print("Dette par année :", [round(d, 1) for d in r['debts']])