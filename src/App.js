import React, { useState } from 'react';
import './App.css';

function App() {
  const [bp, setBp] = useState('');
  const [temperature, setTemperature] = useState('');
  const [reminder, setReminder] = useState('');
  const [logs, setLogs] = useState([]);
  const [statusMessage, setStatusMessage] = useState('');

  const addLog = (message) => {
    setLogs((prevLogs) => [...prevLogs, message]);
  };

  const handleHealthCheck = () => {
    addLog(`🩺 Checking health for BP: ${bp} and Temp: ${temperature}`);

    let [systolic, diastolic] = bp.split('/').map(Number);
    let temp = parseFloat(temperature);
    let message = '';

    if (!systolic || !diastolic || isNaN(temp)) {
      message = '❌ Please enter valid blood pressure and temperature.';
    } else {
      if ((systolic >= 90 && systolic <= 140) && (diastolic >= 60 && diastolic <= 90)) {
        message += '✅ Blood pressure is within normal range. ';
      } else {
        message += '⚠️ Blood pressure is outside normal range. ';
      }

      if (temp >= 97 && temp <= 99.5) {
        message += '✅ Temperature is normal.';
      } else {
        message += '⚠️ Temperature is abnormal.';
      }
    }

    setStatusMessage(`🩺 Health Status: ${message}`);
  };

  const handleSafetyCheck = () => {
    addLog('🛡️ Performing safety check...');
    setStatusMessage('🛡️ Safety Status: All safety parameters are normal. No issues detected.');
  };

  const handleSetReminder = () => {
    addLog(`🔔 Setting reminder: "${reminder}"`);
    if (reminder.trim()) {
      setStatusMessage(`🔔 Reminder Set: "${reminder}"`);
    } else {
      setStatusMessage('⚠️ Please enter a reminder before setting it.');
    }
  };

  const handleEmergencyCall = () => {
    addLog('🚨 Emergency! Contacting medical support...');
    setStatusMessage('🚨 Emergency Activated: Medical help is being contacted immediately!');
  };

  return (
    <div className="app">
      <h1>👵 Elderly Care AI Dashboard</h1>

      <div className="input-group">
        <label><strong>Blood Pressure</strong></label>
        <input value={bp} onChange={(e) => setBp(e.target.value)} placeholder="e.g. 120/80" />
      </div>

      <div className="input-group">
        <label><strong>Temperature</strong></label>
        <input value={temperature} onChange={(e) => setTemperature(e.target.value)} placeholder="e.g. 98.6" />
      </div>

      <div className="input-group">
        <label><strong>Reminder</strong></label>
        <input value={reminder} onChange={(e) => setReminder(e.target.value)} placeholder="e.g. Take medicine at 8PM" />
      </div>

      <div className="button-group">
        <button onClick={handleHealthCheck}>Health Agent</button>
        <button onClick={handleSafetyCheck}>Safety Agent</button>
        <button onClick={handleSetReminder}>Set Reminder</button>
        <button className="emergency" onClick={handleEmergencyCall}>Emergency Call</button>
      </div>

      {/* Output message box */}
      {statusMessage && (
        <div className="status-box">
          <p>{statusMessage}</p>
        </div>
      )}

     
    </div>
  );
}

export default App;
