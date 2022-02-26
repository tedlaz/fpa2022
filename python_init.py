PARAMS = {
    'apo': 's',
    'eos': 's',
    'epon': 's',
    'onom': 's',
    'patr': 's',
    'afm': 's',
    'D36113': '',
    'D36106': '',
    'D36124': '',
    'D36109': '',
    'D36104': '',
    'D36117': '',
    'D361': 'D36113 + D36106 + D36124 + D36109 + D36104 + D36117',
    'D36217': '',
    'D36224': '',
    'D362': 'D36217 + D36224',
    'D36313': '',
    'D36306': '',
    'D36324': '',
    'D36309': '',
    'D36304': '',
    'D36317': '',
    'D363': 'D36313 + D36306 + D36324 + D36309 + D36304 + D36324',
    'D36413': '',
    'D36406': '',
    'D36424': '',
    'D36409': '',
    'D36404': '',
    'D36417': '',
    'D364': 'D36413 + D36406 + D36424 + D36409 + D36404 + D36417',
    'D36517': '',
    'D36524': '',
    'D365': 'D36517 + D36524',
    'D36617': '',
    'D36624': '',
    'D366': 'D36617 + D36624',
    'D367': 'D361 + D362 + D363 + D364 + D365 + D366',
    'D38113': 'D36113 * .13',
    'D38106': 'D36106 * .06',
    'D38124': 'D36124 * .24',
    'D38109': 'D36109 * .09',
    'D38104': 'D36104 * .04',
    'D38117': 'D36117 * .17',
    'D381': 'D38113 + D38106 + D38124 + D38109 + D38104 + D38117',
    'D38217': 'D36217 * .17',
    'D38224': 'D36224 * .24',
    'D382': 'D38217 + D38224',
    'D38313': 'D36313 * .13',
    'D38306': 'D36306 * .06',
    'D38324': 'D36324 * .24',
    'D38309': 'D36309 * .09',
    'D38304': 'D36304 * .04',
    'D38317': 'D36317 * .17',
    'D383': 'D38313 + D38306 + D38324 + D38309 + D38304 + D38317',
    'D38413': 'D36413 * .13',
    'D38406': 'D36406 * .06',
    'D38424': 'D36424 * .24',
    'D38409': 'D36409 * .09',
    'D38404': 'D36404 * .04',
    'D38417': 'D36417 * .17',
    'D384': 'D38413 + D38406 + D38424 + D38409 + D38404 + D38417',
    'D38517': 'D36517 * .17',
    'D38524': 'D36524 * .24',
    'D385': 'D38517 + D38524',
    'D38617': 'D36617 * .17',
    'D38624': 'D36624 * .24',
    'D386': 'D38617 + D38624',
    'D387': 'D381 + D382 + D383 + D384 + D385 + D386',
    'D301': '',
    'D301t': 'D301 + D36413',
    'D302': '',
    'D302t': 'D302 + D36406',
    'D303': '',
    'D303t': 'D303 + D36424 + D36524 + D36624',
    'D304': '',
    'D304t': 'D304 + D36409',
    'D305': '',
    'D305t': 'D305 + D36404',
    'D306': '',
    'D306t': 'D306 + D36417 + D36517 + D36617',
    'D307': 'D301t + D302t + D303t + D304t + D305t + D306t',
    'D342': '',
    'D345': '',
    'D348': '',
    'D349': '',
    'D310': '',
    'D331': 'D301t * .13',
    'D332': 'D302t * .06',
    'D333': 'D303t * .24',
    'D334': 'D304t * .09',
    'D335': 'D305t * .04',
    'D336': 'D306t * .17',
    'D311': 'D307 + D342 + D345 + D348 + D349 + D310',
    'D337': 'D331 + D332 + D333 + D334 + D335 + D336',
    'D312': 'D311 - D364 - D365 - D366',
    'D5400': '',
    'DFPA1': 'D337 - D387',
    'Ddia': 'D5400 - D337 + D387 if D5400 != 0 else 0',
    'D400': '',
    'D402': '-1 * Ddia if Ddia < 0 else 0',
    'D407': '',
    'D410': 'D400 + D402 + D407',
    'D411': '',
    'D422': 'Ddia if Ddia > 0 else 0',
    'D423': '',
    'D428': 'D411 + D422 + D423',
    'D430': 'D387 + D410 - D428',
    'D337430': 'D337 - D430',
    'D470': '-1 * D337430 if D337430 < 0 else 0',
    'D480': 'D337430 if D337430 > 0 else 0',
    'D401': '',
    'D483': '',
    'D401483': 'D401 - D483',
    'DFin': 'D337430 - D401483',
    'D403': '',
    'D404': '',
    'D502': '-1 * DFin if DFin < 0 else 0',
    'D503': '',
    'D505': '',
    'D511': 'DFin if DFin > 0 else 0',
    'D523': '',
}

F2_HTML = """
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
<style>
table, th, td {{
    border: 1px solid black;
    border-collapse: collapse;
}}
th, td {{
    padding: 3px;
}}
</style>
</head>
<body style=" font-size:8pt; font-weight:400; font-style:normal; text-decoration:none;">
<h2><center>ΠΕΡΙΟΔΙΚΗ ΔΗΛΩΣΗ ΦΠΑ</center></h2>
<br>
<p>Από : <b>{apo}</b> Έως :  <b>{eos}</b></p>
<br>
<table border="1" align="center" width="100%" cellspacing="0" cellpadding="4">
  <tbody>
    <tr>
      <td colspan=12>Α. ΠΙΝΑΚΑΣ ΜΕ ΤΑ ΣΤΟΙΧΕΙΑ ΤΟΥ ΥΠΟΚΕΙΜΕΝΟΥ ΣΤΟ ΦΟΡΟ Ή ΛΗΠΤΗ</td>
    </tr>
    <tr>
      <td colspan=12>101.ΕΠΩΝΥΜΟ Ή ΕΠΩΝΥΜΙΑ <b>{epon}</b></td>
    </tr>
    <tr>
      <td colspan=4>102.ΟΝΟΜΑ <br> <b>{onom}</b></td>
      <td style="background-color:#D8EBF9"><center>103<center></td>
      <td colspan=4>ΟΝΟΜΑ ΠΑΤΕΡΑ <br><b>{patr}</b></td>
      <td style="background-color:#D8EBF9"><center>104<center></td>
      <td colspan=2>ΑΦΜ <br><b>{afm}</b></td>
    </tr>
  </tbody>
</table>
<br>
<table>
  <tbody>
    <tr>
      <td colspan=11>Β. ΠΙΝΑΚΑΣ ΕΚΡΟΩΝ - ΕΙΣΡΟΩΝ μετά την αφαίρεση (κατά συντελεστή) των επιστροφών - εκπτώσεων.</td>
    </tr>
    <tr>
      <td rowspan=3><center>Ι. ΕΚΡΟΕΣ, ΕΝΔΟΚ. ΑΠΟΚΤΗΣΕΙΣ & ΠΡΑΞΕΙΣ ΛΗΠΤΗ σε λοιπή Ελλάδα</center></td>
      <td width="3%" style="background-color:#D8EBF9"><center>301</center></td>
      <td align="right" width="9%">{D301t}</td>
      <td width="3%"><center>13</center></td>
      <td width="3%" style="background-color:#D8EBF9" ><center>331</center></td>
      <td align="right" width="7%">{D331}</td>
      <td><center>Αγορές & δαπάνες εσωτερικού</center></td>
      <td width="3%" style="background-color:#D8EBF9" ><center>361</center></td>
      <td align="right" width="9%">{D361}</td>
      <td width="3%" style="background-color:#D8EBF9" ><center>381</center></td>
      <td align="right" width="7%">{D381}</td>
    </tr>
    <tr>
      <td style="background-color:#D8EBF9"><center>302</center></td>
      <td align="right">{D302t}</td>
      <td><center>6</center></td>
      <td style="background-color:#D8EBF9"><center>332</center></td>
      <td align="right">{D332}</td>
      <td><center>Αγορές & εισαγωγές παγίων</center></td>
      <td style="background-color:#D8EBF9"><center>362</center></td>
      <td align="right">{D362}</td>
      <td style="background-color:#D8EBF9"><center>382</center></td>
      <td align="right">{D382}</td>
    </tr>
    <tr>
      <td style="background-color:#D8EBF9"><center>303</center></td>
      <td align="right">{D303t}</td>
      <td><center>24</center></td>
      <td style="background-color:#D8EBF9"><center>333</center></td>
      <td align="right">{D333}</td>
      <td><center>Λοιπες εισαγωγές εκτός παγίων</center></td>
      <td style="background-color:#D8EBF9"><center>363</center></td>
      <td align="right">{D363}</td>
      <td style="background-color:#D8EBF9"><center>383</center></td>
      <td align="right">{D383}</td>
    </tr>
    <tr>
      <td rowspan=3><center>ΙΙ. ΕΚΡΟΕΣ, ΕΝΔΟΚ. ΑΠΟΚΤΗΣΕΙΣ & ΠΡΑΞΕΙΣ ΛΗΠΤΗ στα νησιά Αιγαίου</center></td>
      <td style="background-color:#D8EBF9"><center>304</center></td>
      <td align="right">{D304t}</td>
      <td><center>9</center></td>
      <td style="background-color:#D8EBF9"><center>334</center></td>
      <td align="right">{D334}</td>
      <td><center>Ενδοκοινοτικές αποκτήσεις αγαθών</center></td>
      <td style="background-color:#D8EBF9"><center>364</center></td>
      <td align="right">{D364}</td>
      <td style="background-color:#D8EBF9"><center>384</center></td>
      <td align="right">{D384}</td>
    </tr>
    <tr>
      <td style="background-color:#D8EBF9"><center>305</center></td>
      <td align="right">{D305t}</td>
      <td><center>4</center></td>
      <td style="background-color:#D8EBF9"><center>335</center></td>
      <td align="right">{D335}</td>
      <td><center>Ενδοκοινοτικές λήψεις υπηρεσιών</center></td>
      <td style="background-color:#D8EBF9"><center>365</center></td>
      <td align="right">{D365}</td>
      <td style="background-color:#D8EBF9"><center>385</center></td>
      <td align="right">{D385}</td>
    </tr>
    <tr>
      <td style="background-color:#D8EBF9"><center>306</center></td>
      <td align="right">{D306t}</td>
      <td><center>17</center></td>
      <td style="background-color:#D8EBF9"><center>336</center></td>
      <td align="right">{D336}</td>
      <td><center>Λοιπές πράξεις λήπτη</center></td>
      <td style="background-color:#D8EBF9"><center>366</center></td>
      <td align="right">{D366}</td>
      <td style="background-color:#D8EBF9"><center>386</center></td>
      <td align="right">{D386}</td>
    </tr>
    <tr>
      <td><center><b>ΣΥΝΟΛΟ ΦΟΡ. ΕΚΡΟΩΝ</b></center></td>
      <td style="background-color:#D8EBF9"><center><b>307</b></center></td>
      <td align="right"><b>{D307}</b></td>
      <td><center>ΣΥΝ</center></td>
      <td style="background-color:#D8EBF9"><center><b>337</b></center></td>
      <td align="right"><b>{D337}</b></td>
      <td><center><b>ΣΥΝΟΛΟ ΦΟΡΟΛ. ΕΙΣΡΟΩΝ</b></center></td>
      <td style="background-color:#D8EBF9"><center><b>367</b></center></td>
      <td align="right"><b>{D367}</b></td>
      <td style="background-color:#D8EBF9"><center><b>387</b></center></td>
      <td align="right"><b>{D387}</b></td>
    </tr>
    <tr>
      <td><center>Ενδοκοινοτικές παραδόσεις</center></td>
      <td style="background-color:#D8EBF9"><center>342</center></td>
      <td align="right">{D342}</td>
      <td colspan=3 rowspan=10><center></center></td>
      <td colspan=3><center>δ. ΠΡΟΣΤΙΘΕΜΕΝΑ ΠΟΣΑ ΣΤΟ ΣΥΝΟΛΟ ΦΟΡΟΥ ΕΙΣΡΟΩΝ</center></td>
      <td colspan=2 rowspan=2><center>+</center></td>
    </tr>
    <tr>
      <td><center>Ενδοκοινοτικές παροχές υπηρεσιών</center></td>
      <td style="background-color:#D8EBF9"><center>345</center></td>
      <td align="right">{D345}</td>
      <td><center>Επιστροφή φόρου</center></td>
      <td style="background-color:#D8EBF9"><center>400</center></td>
      <td align="right">{D400}</td>
    </tr>
    <tr>
      <td><center>Εξαγωγές & απαλλαγές πλοίων και αεροσκαφών</center></td>
      <td style="background-color:#D8EBF9"><center>348</center></td>
      <td align="right">{D348}</td>
      <td><center>Λοιπά προστιθ. ποσά</center></td>
      <td style="background-color:#D8EBF9"><center>402</center></td>
      <td align="right">{D402}</td>
      <td style="background-color:#D8EBF9"><center>410</center></td>
      <td align="right">{D410}</td>
    </tr>
    <tr>
      <td><center>Λοιπές εκροές με Δικ Εκπ.</center></td>
      <td style="background-color:#D8EBF9"><center>349</center></td>
      <td align="right">{D349}</td>
      <td><center>Ποσά διακαν.</center></td>
      <td style="background-color:#D8EBF9"><center>407</center></td>
      <td align="right">{D407}</td>
      <td colspan=2 rowspan=3><center>-</center></td>
    </tr>
    <tr>
      <td><center>Εκροές χωρις δικ. εκπτ.</center></td>
      <td style="background-color:#D8EBF9"><center>310</center></td>
      <td align="right">{D310}</td>
      <td colspan=3><center>ε. ΑΦΑΙΡΟΥΜΕΝΑ ΠΟΣΑ ΑΠΟ ΣΥΝΟΛΟ ΦΟΡΟΥ ΕΙΣΡΟΩΝ</center></td>
    </tr>
    <tr>
      <td rowspan=2><center><b>ΣΥΝΟΛΟ ΕΚΡΟΩΝ</b></center></td>
      <td rowspan=2 style="background-color:#D8EBF9"><center><b>311</b></center></td>
      <td rowspan=2 align="right"><b>{D311}<b></td>
      <td><center>ΦΠΑ prorata</center></td>
      <td style="background-color:#D8EBF9"><center>411</center></td>
      <td align="right">{D411}</td>
    </tr>
    <tr>

      <td><center>Λοιπά αφαιρούμ. ποσά</center></td>
      <td style="background-color:#D8EBF9"><center>422</center></td>
      <td align="right">{D422}</td>
      <td style="background-color:#D8EBF9"><center>428</center></td>
      <td align="right">{D428}</td>
    </tr>
    <tr>
      <td rowspan=2><center><b>Κύκλος εργασιών ΦΠΑ</b></center></td>
      <td rowspan=2 style="background-color:#D8EBF9"><center><b>312</b></center></td>
      <td rowspan=2 align="right"><b>{D312}</b></td>
      <td><center>Ποσά διακανονισμών</center></td>
      <td style="background-color:#D8EBF9"><center>423</center></td>
      <td align="right">{D423}</td>
    </tr>
    <tr>
      <td colspan=3><center><b>ΥΠΟΛΟΙΠΟ ΦΟΡΟΥ ΕΙΣΡΟΩΝ</b></center></td>
      <td style="background-color:#D8EBF9"><center><b>430</b></center></td>
      <td align="right"><b>{D430}</b></td>
    </tr>
  </tbody>
</table>
<br>
<table border="1" align="center" width="100%" cellspacing="0" cellpadding="4">
  <tbody>
    <tr>
      <td colspan=7><center><b>Γ. ΠΙΝΑΚΑΣ ΕΚΚΑΘΑΡΙΣΗΣ ΦΟΡΟΥ</b> για καταβολή, έκπτωση ή επιστροφή (κωδ.337 μείον κωδ.430)</center></td>
    </tr>
    <tr>
      <td><center><b>ΠΙΣΤΩΤΙΚΟ ΥΠΟΛΟΙΠΟ</b></center></td>
      <td style="background-color:#D8EBF9"><center>470</center></td>
      <td align="right">{D470}</td>
      <td><center><b>ΧΡΕΩΣΤΙΚΟ ΥΠΟΛΟΙΠΟ</b></center></td>
      <td style="background-color:#D8EBF9"><center>480</center></td>
      <td align="right">{D480}</td>
      <td rowspan=7>Σημειώσεις ......................................</td>
    </tr>
    <tr>
      <td colspan=6>Προσδιορισμός οριστικού ποσού προς καταβολή, έκπτωση ή επιστροφή</td>
    </tr>
    <tr>
      <td><center>Πιστ.υπολ. προηγ. περιόδου</center></td>
      <td style="background-color:#D8EBF9"><center>401</center></td>
      <td align="right">{D401}</td>
      <td><center>Χρεωστικό μέχρι 30€ προηγ. περιόδου</center></td>
      <td style="background-color:#D8EBF9"><center>483</center></td>
      <td align="right">{D483}</td>
    </tr>
    <tr>
      <td><center>Βεβαιωμ. ποσά προηγ.</center></td>
      <td style="background-color:#D8EBF9"><center>403</center></td>
      <td align="right">{D403}</td>
      <td><center>Ποσό που επιστράφηκε</center></td>
      <td style="background-color:#D8EBF9"><center>505</center></td>
      <td align="right">{D505}</td>
    </tr>
    <tr>
      <td><center>Φόρος που έχει δεσμευτεί μέσω τραπεζών</center></td>
      <td style="background-color:#D8EBF9"><center>404</center></td>
      <td align="right"></td>
    </tr>
    <tr>
      <td><center>ΠΟΣΟ για έκπτωση</center></td>
      <td style="background-color:#D8EBF9"><center>502</center></td>
      <td align="right">{D502}</td>
      <td><center>Ποσό προς καταβολή</center></td>
      <td style="background-color:#D8EBF9"><center>511</center></td>
      <td align="right">{D511}</td>
    </tr>
    <tr>
      <td><center>ΑΙΤΟΥΜΕΝΟ ΠΟΣΟ για επιστροφή</center></td>
      <td style="background-color:#D8EBF9"><center>503</center></td>
      <td align="right"></td>
      <td><center>Καταβολή ποσού</center></td>
      <td style="background-color:#D8EBF9"><center>523</center></td>
      <td align="right"></td>
    </tr>
  <tbody>
</table>
<br>
<br>
<br>
<br>

</body>
</html>
"""
