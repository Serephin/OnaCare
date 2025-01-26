def predict_risk(blood_pressure, weight, fetal_heart_rate, systolic_bp, diastolic_bp):
    """
    Predicts risk level based on input health metrics using simple rule-based logic.
    
    Parameters:
        blood_pressure (float): Blood pressure level.
        weight (float): Weight of the individual.
        fetal_heart_rate (float): Fetal heart rate.
        systolic_bp (float): Systolic blood pressure.
        diastolic_bp (float): Diastolic blood pressure.
    
    Returns:
        str: Risk level ('Low', 'Medium', 'High').
    """
    blood_pressure=int(blood_pressure)
    # Basic thresholds for determining risk levels
    if systolic_bp > 140 or diastolic_bp > 90 or blood_pressure > 130:
        if weight > 90 or fetal_heart_rate < 110 or fetal_heart_rate > 160:
            return "High"
        return "Medium"
    elif 120 <= systolic_bp <= 140 or 80 <= diastolic_bp <= 90:
        return "Medium"
    else:
        return "Low"
