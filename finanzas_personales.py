print("========== SISTEMA DE GESTIÓN DE RIQUEZA ==========")

# 1. Definimos las constantes de tu panorama financiero actual
GASTOS_FIJOS = 1500000
DEUDA_TOTAL = 6400000
META_FONDO_EMERGENCIA = 9000000

while True:
    try: 
        # 2. Ingreso mensual
        ganancia_bruta = float(input("\n💰 Ingresa tu ganancia mensual total: $"))
        # 3. Restamos gastos fijos de supervivencia
        dinero_libre = ganancia_bruta - GASTOS_FIJOS
        if dinero_libre <= 0:
         
            print(f" Alerta: Tus ganancias no alcanzan a cubrir tus gastos fijos de ${GASTOS_FIJOS}, por favor revisa tus ingresos o reduce tus gastos.")
            break 
        print(f"\n💵 Dinero libre después de gastos fijos: ${dinero_libre:,.0f}" )

        # 4. Definición de porcentajes estratégicos
        pct_deuda = float(input("📈 ¿Qué % del dinero libre irá a pagar la DEUDA? (ej: 40): "))
        pct_fondo = float(input("🛡️ ¿Qué % del dinero libre irá al FONDO DE EMERGENCIA? (ej: 20): "))

        # Validación de seguridad: Los porcentajes no pueden superar el 100%
        if (pct_deuda + pct_fondo) > 100:
            print("🛑 Error: La suma de los porcentajes supera el 100%. Vuelve a intentar.")
            continue
        # 5. Cálculos de distribución
        abono_deuda = dinero_libre * (pct_deuda / 100)
        abono_fondo = dinero_libre * (pct_fondo / 100)

        # 6. Distribución del sobrante (60% Riqueza / 40% Disfrute)
        sobrante = dinero_libre - abono_deuda - abono_fondo
        
        creacion_riqueza = sobrante * 0.60
        disfrute = sobrante * 0.40
        
        # --- IMPRESIÓN DEL DASHBOARD FINAL ---
        print("\n================ RESUMEN DE DISTRIBUCIÓN ================")
        print(f"🏠 Gastos Fijos:             ${GASTOS_FIJOS:,.0f}")
        print(f"📉 Abono a Deuda ({pct_deuda}%):      ${abono_deuda:,.0f}  (Saldo restante: ${DEUDA_TOTAL - abono_deuda:,.0f})")
        print(f"🛡️ Fondo Emergencia ({pct_fondo}%):   ${abono_fondo:,.0f}  (Meta: ${META_FONDO_EMERGENCIA:,.0f})" f" (Faltante: ${META_FONDO_EMERGENCIA - abono_fondo:,.0f})")
        print("---------------------------------------------------------")
        print(f"Lo que sobra para distribuir: ${sobrante:,.0f}")
        print(f"🚀 Creación de Riqueza (60%): ${creacion_riqueza:,.0f}")
        print(f"🍷 Disfrute (40%):            ${disfrute:,.0f}")
        print("=========================================================")
        
        break # Termina el programa exitosamente
        
    except ValueError:
        print("⚠️ Error: Por favor ingresa solo números, sin puntos ni letras.")