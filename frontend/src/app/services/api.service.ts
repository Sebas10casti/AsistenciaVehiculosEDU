import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})

/** Aqui se definen las peticiones a la API (su backend en python django) */

export class ApiService {
  private http = inject(HttpClient);
  private readonly apiUrl = environment.apiUrl;

  getVehicles() {
    return this.http.get<any[]>(`${this.apiUrl}/vehicles`);
  }

  createVehicle(vehicleData: any) {
    return this.http.post<any>(`${this.apiUrl}/vehicles/`, vehicleData);
  }

  createRegister(registerData: any) {
    return this.http.post<any>(`http://localhost:8000/api/registros/`, registerData);
  }

  getRegisters() {
    return this.http.get<any[]>(`${this.apiUrl}/registros`);
  }

  setRegister(id: string, data: any) {
    return this.http.patch<any>(`${this.apiUrl}/registros/${id}/update_registro/`, data);
  }

  getLastRegister(placa: string) {
    return this.http.get<any>(`${this.apiUrl}/registros/ultimo_registro?placa=${placa}`);
  }
}
