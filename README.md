GPS-Derived PWV using TPS Interpolation
# PWV Interpolation using Thin Plate Spline (TPS)

**Master's Thesis – K.N. Toosi University (2020–2022)**  
**Sheida Chamankar** | sheidachk1223@gmail.com | [ResearchGate](https://researchgate.net/profile/Sheida_Chamankar)

---

## Overview
Modeling **Precipitable Water Vapor (PWV)** from GNSS ZTD using **Thin Plate Spline (TPS)** interpolation over **California**.

**Key Results**:
- **Winter RMSE: 0.6 mm** | **Summer RMSE: 1.62 mm**
- TPS > ANN, Kriging, IDW
- NetCDF mapping

---

## Results Table
| Method  | Winter RMSE (mm) | Summer RMSE (mm) |
|---------|------------------|------------------|
| **TPS** | **0.6**          | **1.62**         |
| IDW     | 0.82             | 2.73             |
| Kriging | 0.97             | 1.98             |
| ANN     | 1.07             | 3.29             |

---

## Code Example
```python
from scipy.interpolate import Rbf
rbf = Rbf(lons, lats, pwv, function='thin_plate')
pwv_grid = rbf(Lon, Lat)
